document.addEventListener("DOMContentLoaded", loadComments);

function loadComments() {
    const comments = JSON.parse(localStorage.getItem(`comments_${postId}`) || '[]');
    const commentList = document.getElementById('commentList');
    const myCommentList = document.getElementById('myCommentList');

    commentList.innerHTML = '';
    myCommentList.innerHTML = '';

    comments.forEach((comment, index) => {
        addCommentToDOM(comment.text, comment.recommendations, comment.userId, index, commentList);
        if (comment.userId === currentUser) {
            addCommentToDOM(comment.text, comment.recommendations, comment.userId, index, myCommentList, true);
        }
    });
}

function saveComments(comments) {
    localStorage.setItem(`comments_${postId}`, JSON.stringify(comments));
}

function addComment() {
    const commentText = document.getElementById('commentText').value;
    if (commentText.trim() === '') return;

    const comments = JSON.parse(localStorage.getItem(`comments_${postId}`) || '[]');
    comments.push({ text: commentText, recommendations: 0, userId: currentUser });
    saveComments(comments);
    loadComments();

    document.getElementById('commentText').value = '';
}

function addCommentToDOM(text, recommendations, userId, commentId, listElement, isMyComment = false) {
    const commentItem = document.createElement('div');
    commentItem.className = 'comment-item';
    commentItem.dataset.commentId = commentId;

    const commentText = document.createElement('span');
    commentText.textContent = text;

    const recommendBtn = document.createElement('span');
    recommendBtn.className = 'recommend-btn';
    recommendBtn.textContent = `추천 (${recommendations})`;

    recommendBtn.addEventListener('click', () => {
        const recommendedComments = JSON.parse(localStorage.getItem(`recommendedComments_${postId}`) || '[]');
        if (recommendedComments.includes(commentId)) return;

        const comments = JSON.parse(localStorage.getItem(`comments_${postId}`) || '[]');
        comments[commentId].recommendations += 1;
        saveComments(comments);

        recommendedComments.push(commentId);
        localStorage.setItem(`recommendedComments_${postId}`, JSON.stringify(recommendedComments));

        recommendBtn.textContent = `추천 (${comments[commentId].recommendations})`;
    });

    commentItem.appendChild(commentText);
    commentItem.appendChild(recommendBtn);

    if (isMyComment) {  // 내 댓글일 경우 삭제 버튼 추가
        const deleteBtn = document.createElement('span');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = '삭제';

        deleteBtn.addEventListener('click', () => {
            const comments = JSON.parse(localStorage.getItem(`comments_${postId}`) || '[]');
            comments.splice(commentId, 1);
            saveComments(comments);

            const recommendedComments = JSON.parse(localStorage.getItem(`recommendedComments_${postId}`) || '[]');
            const updatedRecommendedComments = recommendedComments.filter(id => id !== commentId);
            localStorage.setItem(`recommendedComments_${postId}`, JSON.stringify(updatedRecommendedComments));

            loadComments();
        });

        commentItem.appendChild(deleteBtn);
    }

    listElement.appendChild(commentItem);
}
